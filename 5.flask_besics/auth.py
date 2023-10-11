from flask import Flask, Blueprint, render_template

# Declare a Flask App
app = Flask(__name__)


# Created a Blueprint
auth_controller = Blueprint(
    "auth_controller",
    __name__,
    url_prefix="/",
    template_folder="template-assets/templates",
    static_folder="template-assets/assets",
    static_url_path="assets"
)

@auth_controller.route('/', methods=['GET'])
@auth_controller.route('/login', methods=['GET'])
def login():
    return render_template("auth/login.html")


@auth_controller.route('/registration', methods=['GET'])
def registration():
    return render_template("auth/registration.html")


@auth_controller.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("auth/dashboard.html")

@auth_controller.route('/forgot-password', methods=['GET'])
def forgot_password():
    return render_template("auth/forgot-password.html")

@auth_controller.route('/invalid-token', methods=['GET'])
def invalid_token():
    return render_template("auth/invalid-token.html")

@auth_controller.route('/otp', methods=['GET'])
def otp():
    return render_template("auth/otp.html")

@auth_controller.route('/verification-success', methods=['GET'])
def verification_success():
    return render_template("auth/verification-success.html")

@auth_controller.route('/reset-success', methods=['GET'])
def reset_success():
    return render_template("auth/reset-success.html")


@auth_controller.route('/404', methods=['GET'])
def not_found():
    return render_template("auth/404.html")


@auth_controller.route('/500', methods=['GET'])
def error():
    return render_template("auth/500.html")

@auth_controller.route('/set-password', methods=['GET'])
def set_password():
    return render_template("auth/set-password.html")




# Register the Blueprint
app.register_blueprint(auth_controller)


if __name__ == '__main__':
    app.run(debug=True)
