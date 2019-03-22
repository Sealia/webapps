from django import forms

class SeqContentForm(forms.Form):
	sequence = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter sequence'}),min_length=5, required=True)
	word_size = forms.IntegerField(required=True)

	def clean_sequence(self):
		sequence = self.cleaned_data["sequence"]
		return sequence.upper()

	def clean_word_size(self):
		word_size = self.cleaned_data["word_size"]
		if word_size < 1:
			raise forms.ValidationError("Word size must be greater than 1")
		return word_size

	def clean(self):
		sequence=self.cleaned_data.get("sequence", None)
		word_size= self.cleaned_data.get("word_size", None)
		if sequence and word_size:
			if len(sequence) < word_size:
				raise forms.ValidationError("Sequence cannot be shorter than word size")

class RevCompForm(forms.Form):
	sequence = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter sequence'}),min_length=5, required=True)
	Methods=(('reverse','reverse'),('complement','complement'),('reverse complement','reverse complement'))
	select=forms.CharField(widget=forms.Select(choices=Methods))

	def clean_select(self):
		select=self.cleaned_data["select"]
		return select

	def clean_sequence(self):
		sequence = self.cleaned_data["sequence"]
		return sequence.upper()
