from typing import Dict
import pytz
from datetime import datetime, timedelta
import requests
import streamlit as st

import config

def set_user_details() -> None:
    """Saves the user details to the session state."""
    user_details = get_user_details()
    st.session_state.name = user_details["first_name"]
    st.session_state.credentials_set = user_details["credentials_set"]
    st.session_state.organisation_name = user_details["organisation_name"]
    st.session_state.organisation_kvk = user_details["organisation_kvk"]
    st.session_state.default_project_number = user_details["default_project_number"]
    st.session_state.user_profile_url = user_details["url"]

def get_user_details() -> Dict[str, str]:
    """Retreives userprofile information from the api."""
    url = f"{config.BASE_URL}/api/userprofile"

    r = requests.get(
        url=url,
        headers=st.session_state.headers,
    )
    r.raise_for_status()

    return r.json()["results"][0]

def patch_user_profile() -> None:
    """Updates the userprofile on the user profile enpoint."""
    payload = {}
   
    if st.session_state["change-default-project-number"]:
        payload["default_project_number"] = st.session_state["change-default-project-number"]

    if st.session_state["change-bro-user-token"]:
        payload["bro_user_token"] = st.session_state["change-bro-user-token"]
    
    if st.session_state["change-bro-user-password"]:
        payload["bro_user_password"] = st.session_state["change-bro-user-password"]
        
    r = requests.patch(
        url=st.session_state.user_profile_url,
        headers=st.session_state.headers,
        json= payload,
    )
    r.raise_for_status()

    if r.status_code == 200:
        st.session_state["user_profile_updated_status"] = True
    else:
        st.session_state["user_profile_updated_status"] = False

def get_endpoint_count(endpoint: str) -> int:
    """Gets the count on a given endpoint"""
    url = f"{config.BASE_URL}/api/{endpoint}/"

    r = requests.get(
        url=url,
        headers=st.session_state.headers,
    )
    r.raise_for_status()

    return r.json()["count"]

def lookup_most_recent_datetime(endpoint: str) -> str:
    """Checks the most recent import or upload task in the API."""
    url = f"{config.BASE_URL}/api/{endpoint}/?status=COMPLETED&kvk_number={st.session_state.organisation_kvk}"
    r = requests.get(
        url=url,
        headers=st.session_state.headers,
    )
    r.raise_for_status()

    last_update = datetime.fromisoformat(r.json()["results"][0]["updated_at"])
    return last_update

def start_import_tasks(*args: list[str], **kwargs) -> None:
    """Start an importtask in the api based on the provided domains.
    
    Only runs after a validation, where is checked whether there has been an import
    task has been done in the last hour. This is to prevent an overload on the BRO.
    """
    kvk_number = kwargs.get("kvk_number")
    
    if validate_import_request():
        url = f"{config.BASE_URL}/api/importtasks/"
        for domain in args:
            r = requests.post(
                url=url,
                headers=st.session_state.headers,
                json={"bro_domain":domain, "kvk_number":kvk_number}
            )
            r.raise_for_status()

        st.session_state["import_task_started"] = True

    else:
        st.session_state["import_task_started"] = False

def validate_import_request() -> bool:
    timezone = pytz.timezone('CET')
    now = datetime.now(timezone)
    most_recent_import_datetime = lookup_most_recent_datetime("importtasks")
    check = (now - most_recent_import_datetime) > timedelta(hours=1)
    
    return True if check else False