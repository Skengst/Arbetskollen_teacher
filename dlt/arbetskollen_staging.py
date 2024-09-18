#%%
import dlt
import requests
import json
from pathlib import Path
import os

def _get_ads(url_for_search, params):
    headers = {"accept": "application/json"}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode("utf8"))

@dlt.resource(write_disposition="append")  # change to "append" for batching
def jobsearch_resource(params, batch_size=100, max_batches=None):
    url = "https://jobsearch.api.jobtechdev.se"
    url_for_search = f"{url}/search"
    
    offset = 0
    batch_count = 0
    
    while True:
        params["offset"] = offset
        ads = _get_ads(url_for_search, params)["hits"]

        if not ads:
            break

        for ad in ads:
            yield ad

        offset += batch_size
        batch_count += 1

        if max_batches is not None and batch_count >= max_batches:
            break

def run_pipeline(query, table_name, max_batches=None):
    pipeline = dlt.pipeline(
        pipeline_name="jobsearch_teacher_pipeline",
        destination="snowflake",
        dataset_name="staging", 
    )

    params = {"q": query, "limit": 100} 

    load_info = pipeline.run(jobsearch_resource(params=params, max_batches=max_batches), table_name=table_name)
    print(load_info)

if __name__ == "__main__":
    working_directory = Path(__file__).parent
    os.chdir(working_directory)

    query = "lärare"
    table_name = "jobsearch_teacher_data"

    run_pipeline(query, table_name, max_batches=10)

# %%