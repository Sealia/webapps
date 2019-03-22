from django.shortcuts import render
from .forms import SeqContentForm, RevCompForm
from . import utils

def seqcontent_view(request):
	if request.method == 'POST':
		form = SeqContentForm(request.POST)
		if form.is_valid():
			seq = form.cleaned_data['sequence']
			word_size = form.cleaned_data['word_size']
			d =utils.count_words(seq,word_size)
			# for i in range(0, len(sequence)-word_size+1):
			# 	word = sequence[i:i+word_size]
			# 	if word not in d:
			# 		d[word]= 0
			# 	d[word]+= 1
			return render(request,'biotools/seqcontent.html', {'results':d})
	else:
		form = SeqContentForm()
	return render(request,'biotools/seqcontent.html',{'form':form})

def revcomp_view(request):
	if request.method == 'POST':
		form = RevCompForm(request.POST)
		if form.is_valid():
			seq=form.cleaned_data['sequence']
			a = form.cleaned_data['select']
			w =[]
			if a == 'complement':
				w=utils.complement(seq)
				seq=w;
			if a == 'reverse':
				w=utils.reverse(seq)
			if a == 'reverse complement':
				w=utils.complement(seq)
				w=utils.reverse(w)


			return render(request,'biotools/revcomp.html',{'results':w})
	else:
		form=RevCompForm();
	return render(request,'biotools/revcomp.html',{'form':form})
