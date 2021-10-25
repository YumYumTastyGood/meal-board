import re
import settings
import requests
from flask import request
from __main__ import app

recompiler = re.compile("[^ \u3131-\u3163\uac00-\ud7a3]+")


@app.route("/meal", methods=["GET"])
def get_meal():
    paramdict = request.args.to_dict()
    # when = paramdict.get("when", "")
    # if not when:
    # return {"message": "when is required"}, 400
    begin = paramdict.get("begin", None)
    if not begin:
        return {"message": "begin is required"}, 400
    end = paramdict.get("end", None)
    if not end:
        return {"message": "end is required"}, 400
    if int(begin) > int(end):
        return {"message": "begin must be less than end"}, 400
    region_code = paramdict.get("region_code", None)
    if not region_code:
        return {"message": "region_code is required"}, 400
    school_code = paramdict.get("school_code", None)
    if not school_code:
        return {"message": "school_code is required"}, 400

    response = requests.get(
        f"{settings.NEIS_API_URL}?Type=json&ATPT_OFCDC_SC_CODE={region_code}&SD_SCHUL_CODE={school_code}&MMEAL_SC_CODE=2&MLSV_FROM_YMD={begin}&MLSV_TO_YMD={end}"
    )
    data = response.json()
    meal_info_list = data.get("mealServiceDietInfo")[1].get("row")
    result = {
        meal_info.get("MLSV_FROM_YMD", ""): {
            "MMEAL_SC_CODE": meal_info.get("MMEAL_SC_CODE", ""),
            "MMEAL_SC_NM": meal_info.get("MMEAL_SC_NM", ""),
            # "DDISH_NM": "".join(meal_info.get("DDISH_NM", "").split("<br/>")),
            "DDISH_NM": [
                recompiler.sub("", x)
                for x in meal_info.get("DDISH_NM", "").split("<br/>")
            ],
        }
        for meal_info in meal_info_list
    }

    return {"result": result}, 200
