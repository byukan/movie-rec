from flask import render_template, request, redirect, url_for


# This class allows for view function testing (testing not the website
# appearance, but rather the behavior of the underlying modules).
class ViewFunctionResponse:
    def __init__(self):
        self.render_response = False
        self.redirect_response = False

        self.render_template = None
        self.redirect_view = None
        self.kwargs = None

    def create_render_response(self, template_name, kwargs):
        self.render_response = True
        self.redirect_response = False
        self.render_template = template_name
        self.kwargs = kwargs

    def create_redirect_response(self, view_function, kwargs):
        self.redirect_response = True
        self.render_response = False
        self.redirect_view = view_function
        self.kwargs = kwargs

    def get_http_response(self):
        if self.render_response:
            return render_template(self.render_template, **self.kwargs)
        elif self.redirect_response:
            return redirect(url_for(self.redirect_view, **self.kwargs))
        else:
            return "Not Found", 404
