import queue
import requests

q = queue.Queue()
q_style = ''

endpoint = 'https://jmai.art'
path = '/api/prompt/make'
url = endpoint + path


class ComfyUI_Prompt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        styles = ['随机','女孩','设计','风景','风格','摄影','恐怖','怪物','手办','微观','中国风','剪影','赛博','电影','诡异','3D']
        return {
            "required": {
                "style": (styles,),
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

    def random_prompt(self, style, seed, log_prompt):
        global q_style
        if q.empty() or q_style != style:
            q.queue.clear()
            # Build request
            headers = {'Content-Type': 'application/json'}
            payload = {
                'seed': seed,
                'name': style
            }

            # Send request
            r = requests.get(url, params=payload, headers=headers)
            q_style = style
            print(f"style: {style}")
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
