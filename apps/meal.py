import re
import settings
import requests
from flask import request
from flask_restx import Resource, Namespace

recompiler = re.compile("[^ \u3131-\u3163\uac00-\ud7a3]+")

Meal = Namespace("Meal")


@Meal.route("")
class MealInfo(Resource):
    """
    급식정보를 제공하기위한 API
    """

    def get(self):
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


@Meal.route("/police")
class MealPolice(Resource):
    """
    밥경찰 리스트 저장 관리용
    """

    def get(self):
        response = {}


@Meal.route("/theif")
class MealTheif(Resource):
    """
    밥도둑 정보 저장 관리용
    """

    def get(self):
        response = {}
