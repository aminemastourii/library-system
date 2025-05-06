from django import forms

class BorrowForm(forms.Form):
    pages = forms.IntegerField(min_value=11, help_text="Enter number of pages to borrow (from page 11 onwards)")
    duration = forms.IntegerField(min_value=1, max_value=30, label="Duration (days)")
    def __init__(self, *args, **kwargs):
        total_pages = kwargs.pop('total_pages')
        super().__init__(*args, **kwargs)
        self.fields['pages'].widget.attrs['max'] = total_pages
        self.fields['pages'].widget.attrs['placeholder'] = f"Max {total_pages} pages"
