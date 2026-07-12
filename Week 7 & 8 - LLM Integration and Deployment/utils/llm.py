import ollama


def generate_report(detections, inspection_date):

    if len(detections) == 0:
        return "No defects were detected. The steel surface appears to be defect-free."

    defect_list = "\n".join(
        [
            f"- {d['defect']} ({d['confidence']}%)"
            for d in detections
        ]
    )

    prompt = f"""
You are an experienced Industrial Quality Assurance Engineer.

Generate a professional inspection report in exactly this format:


Date: {inspection_date}

Detected Defects:
{defect_list}

Include these sections:

1. Inspection Summary
2. Severity Level
3. Recommended Corrective Actions


Do NOT include:
- Location
- Material/Component
- Part Number
- Inspector's Name
- Signature
- Quality Engineer
- Approval section
- Placeholder text like [Insert Date] or [Insert Name]

End the report after the Final Recommendation section.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]