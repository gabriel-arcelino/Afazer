from flask_login import LoginManager

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    #since the user_id is just the primary key of our user table, use it in the query for the user
    print("Id: ", user_id)

def iniciar_app(app,webui):
    login_manager.login_view = 'webui.login'
    login_manager.init_app(app)

