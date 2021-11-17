import re
import settings
import requests
from flask import request, Blueprint
from apps.interfaces.meal import NeisMealValidator

recompiler = re.compile("[^ \u3131-\u3163\uac00-\ud7a3]+")

meal = Blueprint("meal", __name__, url_prefix="/meal")


@meal.route("/", methods=["GET"])
def get_meal():
    query = NeisMealValidator(request.args, meta={"csrf": False})
    if not query.validate():
        return jsonify(query.errors), 400
    begin = query.data["begin"]
    end = query.data["end"]
    if int(begin) > int(end):
        return {"message": "begin must be less than end"}, 400
    region_code = query.data["region_code"]
    school_code = query.data["school_code"]
    response = requests.get(
        f"{settings.NEIS_API_URL}?Type=json&ATPT_OFCDC_SC_CODE={region_code}&SD_SCHUL_CODE={school_code}&MMEAL_SC_CODE=2&MLSV_FROM_YMD={begin}&MLSV_TO_YMD={end}"
    )
    data = response.json()
    meal_info = data.get("mealServiceDietInfo")
    if not meal_info:
        return {"result": "success", "message": "no meal"}, 400
    meal_info_list = meal_info[1].get("row")
    result = {
        meal_info.get("MLSV_FROM_YMD", ""): {
            "MMEAL_SC_CODE": meal_info.get("MMEAL_SC_CODE", ""),
            "MMEAL_SC_NM": meal_info.get("MMEAL_SC_NM", ""),
            "DDISH_NM": [
                recompiler.sub("", x)
                for x in meal_info.get("DDISH_NM", "").split("<br/>")
            ],
        }
        for meal_info in meal_info_list
    }

    return {"result": result}, 200
