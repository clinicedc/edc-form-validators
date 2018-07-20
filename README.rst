|pypi| |travis| |coverage|

edc-form-validators
-------------------

Form validator classes for ModelForms


ModelForm ``FormValidator``
---------------------------

``FormValidator`` simplifies common patterns used in ``ModelForm.clean``. For example, if there is a response to field A then there should not a be response to B and visa-versa.

Declare a form with it's ``form_validator`` class and use ``FormValidatorMixin``:

.. code-block:: python

    class MyFormValidator(FormValidator):

        def clean(self):
            self.required_if(
                YES,
                field='f1',
                field_required='f2')
            ...

    class MyModelForm(FormValidatorMixin, forms.ModelForm):

        form_validator_cls = MyFormValidator

        class Meta:
            model = TestModel
            fields = '__all__'
 

Testing
-------

Test the ``form_validator`` without having to instantiate the ``ModelForm``:

.. code-block:: python

    def test_my_form_validator(self):
        options = {
            'f1': YES,
            'f2': None}
        form_validator = MyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('f2', form_validator._errors)


.. |pypi| image:: https://img.shields.io/pypi/v/edc-form-validators.svg
    :target: https://pypi.python.org/pypi/edc-form-validators
    
.. |travis| image:: https://travis-ci.org/clinicedc/edc-form-validators.svg?branch=develop
    :target: https://travis-ci.org/clinicedc/edc-form-validators
    
.. |coverage| image:: https://coveralls.io/repos/github/clinicedc/edc-form-validators/badge.svg?branch=develop
    :target: https://coveralls.io/github/clinicedc/edc-form-validators?branch=develop
    