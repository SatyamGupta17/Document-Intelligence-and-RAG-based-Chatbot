# # extraction/extractor.py

# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential
# from app.config import DOC_ENDPOINT, DOC_KEY

# client = DocumentAnalysisClient(
#     endpoint=DOC_ENDPOINT,
#     credential=AzureKeyCredential(DOC_KEY)
# )

# def extract_text(file_path):

#     with open(file_path, "rb") as f:

#         poller = client.begin_analyze_document(
#             "prebuilt-layout",
#             document=f
#         )

#     result = poller.result()

#     text = ""

#     for page in result.pages:
#         for line in page.lines:
#             text += line.content + "\n"

#     return text

import fitz

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text