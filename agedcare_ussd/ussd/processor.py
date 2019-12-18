from agedcare_ussd.models import Session
from agedcare_ussd.ussd.constants import SERVICE_CODE ,PHONE_NUMBER ,SESSION_ID  ,OPERATOR ,SEQUENCE ,MESSAGE ,CLIENT_STATE , RESPONSE, TIMEOUT , RELEASE , GATEWAY, RESPONSE_TYPE , INITIATION , START, MAIN_MENU, ONE,TWO,THREE,FOUR, STAGE_ENTER_FULLNAME , STAGE_ENTER_TELEPHONE , STAGE_SELECT_GENDER , STAGE_ENTER_AMOUNT , STAGE_ENTER_MOMO , STAGE_BLOOD_GLUCOSE , STAGE_BLOOD_PRESSURE , STAGE_BLOOD_CHOLESTEROL , STAGE_BLOOD_LEVEL , STAGE_WEIGHT_LEVEL , STAGE_HELP , FINISH
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned



     
     

class Ussd(object):

    def __init__(self, data):
        self.service_code = data.get(SERVICE_CODE)
        self.phone_number = data.get(PHONE_NUMBER)
        self.session_id = data.get(SESSION_ID)
        self.operator = data.get(OPERATOR)
        self.sequence = data.get(SEQUENCE)
        self.message = data.get(MESSAGE)
        self.stage = data.get(CLIENT_STATE)
        self.response = data.get(RESPONSE_TYPE)
        self.gateway = data.get(GATEWAY)
        self.session = self.get_or_create_session()
    

    def get_stage(self):
        return self.session.stage
    
    def get_or_create_session(self):
        session, created = Session.objects.get_or_create(session_id=self.session_id,gateway=self.gateway,phone_number=self.phone_number,defaults=dict(operator=self.operator))
        if created:
            session.set_stage(START)
        return session
    

    def save_data(self, data):
        try:

            record, created = Session.objects.update_or_create(session_id=self.session_id,
                                                                service_code=self.service_code,
                                                                operator=self.operator,
                                                                phone_number=self.phone_number,
                                                                stage=self.stage)
            record.save_data(data)
        except Session.DoesNotExist:
            pass
    

    def finish(self, process=None):
        text = '' 
        response_type = RELEASE
        client_state = FINISH

        if process == 'registration':
            text = 'Thank You for Subscribing'
        elif process == 'saving':
            text = 'Saving'
        
        elif process == 'health':
            text = 'text'
            
            
        return self.process_response(message=text,response_type=response_type,client_state=client_state)
    
    def process_request(self):

        if self.response == INITIATION:
            return self.welcome_option()
        elif self.response == RESPONSE:
            stage = self.get_stage()
            if stage == MAIN_MENU:
                return self.main_menu_options()
            else:
                return self.get_next_response(client_state=stage)
    
    def get_next_response(self, client_state):
        
        if client_state == STAGE_ENTER_FULLNAME:

            if self.message == '':
                return self.register_enter_fullname()
            # save
            return self.register_enter_telephone()
        

        elif client_state == STAGE_ENTER_TELEPHONE:

            if self.message == '':
                return self.register_enter_telephone()
            # save 
            return self.register_enter_gender()
        
        elif client_state == STAGE_SELECT_GENDER:

            if self.message == '':
                return self.register_enter_gender()

            # save 
            return self.finish(process='registration')
        
        elif client_state == STAGE_ENTER_AMOUNT:

            if self.message == '':
                return self.saving_amount()
            

            return self.saving_momo()
        
        elif client_state == STAGE_ENTER_MOMO:

            if self.message == '':
                return self.saving_momo()
            

            return self.finish(process='saving')
        
        elif client_state == STAGE_BLOOD_GLUCOSE:

            if self.message == '':
                return self.health_record_glucose()
            

            return self.health_record_blood_pressure()
        
        elif client_state == STAGE_BLOOD_PRESSURE:

            if self.message == '':
                return self.health_record_blood_pressure()
            

            return self.health_record_cholesterol()
        
        elif client_state == STAGE_BLOOD_CHOLESTEROL:

            if self.message == '':
                return self.health_record_cholesterol()
            
            return self.health_record_blood_level()
        

        elif client_state == STAGE_BLOOD_LEVEL:

            if self.message == '':
                return self.health_record_cholesterol()
            

            return self.health_record_weight()
        
        elif client_state == STAGE_WEIGHT_LEVEL:

            if self.message == '':
                return self.health_record_weight()
            

            return self.finish(process='health')
            






            

    def welcome_option(self):
        return self.display_main_menu()
    
    def main_menu_options(self):
        if self.message in [ONE,TWO,THREE,FOUR]:

            if self.message == ONE:
                return self.register_enter_fullname()

            elif self.message == TWO:
                return self.saving_amount()
            
            elif self.message == THREE:
                return self.health_record_glucose()
            
            elif self.message == FOUR:
                return self.help()

        else:
            return self.display_main_menu(error=True)
    
    def display_main_menu(self, error=False):
        message = 'Welcome to AgedCare \n 1. Register \n 2. AgedCare \n 3. Health Fund'

        if error:
            message = 'Invalid Option Selected \n 1. Register \n 2. AgedCare \n 3. Health Fund'
        
        stage = MAIN_MENU
        response_type = RESPONSE
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    

    def register_enter_fullname(self, error=False):


        if error:
            message = 'Please enter fullname'


        stage = STAGE_ENTER_FULLNAME
        response_type = RESPONSE
        message = 'Enter FullName'
        return self.process_response(message=message,response_type=response_type,client_state=stage)


    def register_enter_telephone(self, error=False):

        if error:
            message = 'Please enter phonenumber'
        stage = STAGE_ENTER_TELEPHONE
        response_type = RESPONSE
        message = 'Please enter phonenumber'
        return self.process_response(message=message,response_type=response_type,client_state=stage)

    def register_enter_gender(self, error=False):
        
        if error:
            message = 'Invalid Option. \n 1. M (Male) \n 2. F (Female)'
        
        stage = STAGE_SELECT_GENDER
        response_type = RESPONSE
        message = 'Gender Type \n 1. M (Male) \n 2. F (Female)'
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    
    def register_finish(self, error=False):

        pass
        


    def saving_amount(self, error=False):

        if error:
            message = 'Please enter amount'
        
        stage = STAGE_ENTER_AMOUNT
        response_type = RESPONSE
        message = 'Please enter amount'
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    
    
    def saving_momo(self, error=False):

        if error:
            message = 'Please enter Mobile Money Number'
        
        stage = STAGE_ENTER_MOMO
        response_type = RESPONSE
        message = 'Please enter Mobile Money Number'
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    

    def health_record_glucose(self, error=False):

        if error:
            message = 'Enter your blood glucose'
        

        stage = STAGE_BLOOD_GLUCOSE
        response_type = RESPONSE
        message = 'Please enter your Blood Glucose'
        return self.process_response(message=message,response_type=response_type,client_state=stage)

    def health_record_blood_pressure(self, error=False):

        if error:
            message = 'Please enter your Blood pressure'
        

        stage = STAGE_BLOOD_PRESSURE
        response_type = RESPONSE
        message = 'Enter your Blood Pressure'
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    

    def health_record_cholesterol(self, error=False):

        if error:
            message = 'Please Enter your Blood cholesterol'
        
        stage = STAGE_BLOOD_CHOLESTEROL
        response_type = RESPONSE
        message = 'Enter your blood cholesterol'
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    

    def health_record_blood_level(self, error=False):

        if error:
            message = 'Please Enter your Blood Level'
        
        stage = STAGE_BLOOD_LEVEL
        response_type = RESPONSE
        message = 'Enter your Blood Level'
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    

    def health_record_weight(self, error=False):

        if error:
            message = 'Please Enter your weight'
        

        stage = STAGE_WEIGHT_LEVEL
        response_type = RESPONSE
        message = 'Enter your weight'
        return self.process_response(message=message,response_type=response_type,client_state=stage)

        


    def help(self, error=False):
        stage = STAGE_HELP
        response_type = RELEASE
        message = 'Contact Phone Number'
        return self.process_response(message=message,response_type=response_type,client_state=stage)

    def exit(self):
        message = 'Thank you '
        client_state = FINISH
        response_type = RELEASE
        return self.process_response(message=message,response_type=response_type,client_state=client_state)
    
    def process_response(self, message, response_type, client_state):
        session = self.session
        session.set_stage(client_state)
        return dict(message=message, stage=client_state,response_type=response_type)
