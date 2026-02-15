from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
from docquery import app
from .forms import DocUploadForm
import os
from .main import LLMPipeline
import tempfile

LLM =LLMPipeline()

@app.route("/", methods = ['GET', 'POST'])
def home():

    if request.method == 'POST':
        file = request.files['pdf_file']

        if file and file.filename != '':
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
                tmp.write(file.read())
                pdf_path = tmp.name


            document = LLM.loading_documents(doc_path=pdf_path)
            vectorname, vectorpath = LLM.chunk_embed_store(document)

            data_to_pass = {'vectorname': vectorname,
                            'vectorpath': vectorpath}

            session['vector_data'] = data_to_pass

            return redirect(url_for('chat'))

    return render_template("index.html")


@app.route("/chat", methods=['GET', "POST"])
def chat():

    if request.method == 'GET':
        return render_template('chat.html')

    if request.method == 'POST':
        vector_data = session.get('vector_data')
        vectorstore = LLM.load_vectorstore(vectorpath=vector_data['vectorpath'])

        data = request.get_json('message')
        user_input = data.get('message')

        retreiver = LLM.Retrieve(vectorstore)
        docs = retreiver.invoke(user_input)
        answer = LLM.respond(docs, user_input)



        return jsonify({"answer": answer})


    return render_template("chat.html")










