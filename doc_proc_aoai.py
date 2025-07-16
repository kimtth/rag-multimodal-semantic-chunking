import os
from loguru import logger
from openai import AzureOpenAI

AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def img_desc_from_azure_openai(
    client: AzureOpenAI,  # Azure OpenAI client
    img_base64: str,  # Base64 encoded image string
):
    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this figure/image from a document and provide a detailed description. Focus on key elements, any text or labels visible in the image.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{img_base64}"},
                        },
                    ],
                }
            ],
        )
        description = response.choices[0].message.content.strip()
        logger.info(f"Generated description: {description}")

        return description
    except Exception as e:
        logger.error(f"Error generating image description: {str(e)}")
        return ""
