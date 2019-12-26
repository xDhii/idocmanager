# idocmanager


This is an automated tool to generate and send IDOC documents to TF.
Found a BUG?
Email us!

adriano.valumin@sovos.com

tayna.blasques@sovos.com

---

It was added a file called 'loopidocmanager.py' which makes it possible to do a loop on IDOC creation
'''
for /l %%x in (1, 1, 10) do (
	.\idocmanager.py "b" "a" "a" "n" "n"
)
'''
You can substitute 10 by the number of times that you want that Windows execute it

Besides that, now it is possible to run the IDOCManager inserting arguments through command line
'''
.\idocmanager.py "country" "document_type" "tax_id" "send_it_to_vm" "create_another_document"
'''