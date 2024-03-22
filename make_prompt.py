import queue
import requests

q = queue.Queue()

endpoint = 'https://jmai.art'
path = '/api/prompt/make'
url = endpoint + path


class ComfyUI_Prompt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("STRING", {"multiline": False}),
                "log_prompt": (["No", "Yes"], {"default": "Yes"}),
            },
        }

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_positive',)
    FUNCTION = "random_prompt"
    CATEGORY = "ComfyUI_Mexx"

    def random_prompt(self, seed, log_prompt):
        if q.empty():
            # Build request
            headers = {'Content-Type': 'application/json'}
            payload = {'seed': seed}

            # Send request
            r = requests.get(url, params=payload, headers=headers)
            result = r.json()
            q.put(result["data"][0]["prompt"])
            q.put(result["data"][1]["prompt"])
            q.put(result["data"][2]["prompt"])
            q.put(result["data"][3]["prompt"])
            q.put(result["data"][4]["prompt"])
            q.put(result["data"][5]["prompt"])
            q.put(result["data"][6]["prompt"])
            q.put(result["data"][7]["prompt"])
            q.put(result["data"][8]["prompt"])
            q.put(result["data"][9]["prompt"])

        prompt = q.get()
        if log_prompt == "Yes":
            print(f"Prompt: {prompt}")
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "ComfyUI_Prompt": ComfyUI_Prompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_Prompt": "ComfyUI_Prompt"
}
