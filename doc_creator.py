from docxtpl import DocxTemplate
def doc_creator(referat_mavzusi,referat_izohi ):
    doc = DocxTemplate("my_word_template.docx")
    context = { 'referat_mavzusi' : f"{referat_mavzusi}",
                'referat_izohi': f"{referat_izohi}"}
    doc.render(context)
    doc.save("generated_doc.docx")