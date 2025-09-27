from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1

summarize = pipeline('summarization', model='t5-small', device=device)

def summarize_text(text):
    if len(text.split()) < 10:
        return text

    try:
        summary = summarize(text, max_length=50, min_length=10, do_sample=False)
        return summary[0]['summary_text'] # Looking to only the first result of the summary

    except Exception:
        return text
