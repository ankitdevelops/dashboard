from django.contrib.auth.decorators import user_passes_test


def teacher_only(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_teacher, login_url="login"
    )(view_func)
    return decorated_view_func
