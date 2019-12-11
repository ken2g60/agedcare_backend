from advisory_ussd.models import Session
from advisory_ussd.ussd.constants import SERVICE_CODE ,PHONE_NUMBER ,SESSION_ID  ,OPERATOR ,SEQUENCE ,MESSAGE ,CLIENT_STATE ,RESPONSE,TIMEOUT , RELEASE , GATEWAY, RESPONSE_TYPE , INITIATION , START, MAIN_MENU, ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT, FINISH
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


from advisory_ussd.models import MSubscribe


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
            print('error in database')
    

    def finish(self, process=None):
        text = '' 
        response_type = RELEASE
        client_state = FINISH

        if process == 'end_subscription':
            text = 'Thank You for Subscribing'
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
        pass

            

    def welcome_option(self):
        return self.display_main_menu()
    
    def main_menu_options(self):
        if self.message in [ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN]:

            if self.message == ONE:
                return self.subscribe()

            elif self.message == TWO:
                return self.subscribe()

            elif self.message == THREE:
                return self.subscribe() 
            elif self.message == FOUR:
                return self.subscribe()
            elif self.message == FIVE:
                return self.subscribe() 
            elif self.message == SIX:
                return self.subscribe()
            elif self.message == SEVEN:
                return self.subscribe()

        else:
            return self.display_main_menu(error=True)
    
    def display_main_menu(self, error=False):
        message = 'Welcome to AgedCare \n 1.'

        if error:
            message = 'Try Again .'
        
        stage = MAIN_MENU
        response_type = RESPONSE
        return self.process_response(message=message,response_type=response_type,client_state=stage)
    

        
    def exit(self):
        message = 'Thank you for using Madvisory'
        client_state = FINISH
        response_type = RELEASE
        return self.process_response(message=message,response_type=response_type,client_state=client_state)
    
    def process_response(self, message, response_type, client_state):
        session = self.session
        session.set_stage(client_state)
        return dict(message=message, stage=client_state,response_type=response_type)
