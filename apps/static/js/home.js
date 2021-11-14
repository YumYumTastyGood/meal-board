const searchSchool = () => {
  const schoolName = document.getElementById('school-textfield').value
  const selector = document.getElementById('location-selector')
  const regionCode = selector.options[selector.selectedIndex].value
  $.ajax({
    type: "GET",
    url: "https://meal-board.herokuapp.com/school",
    data: {
      'location': regionCode,
      'school': schoolName
    },
    success: function (response) {
      const school_list = response.school_list
      const modal = document.getElementById('school-list-modal')
      modal.innerHTML = ''
      for (school_info of school_list) {
        let schoolDiv = document.createElement('div')
        const schoolInfo = document.createTextNode(school_info.school_name)
        schoolDiv.appendChild(schoolInfo)
        schoolDiv.setAttribute('value', school_info.school_code)
        schoolDiv.setAttribute('name', school_info.school_name)
        schoolDiv.setAttribute('onclick', `setSchoolInfo(${school_info.school_code}, "${school_info.school_name}")`)
        modal.append(schoolDiv)
      }
    }
  })
}

const setSchoolInfo = (school_code, school_name) => {
  document.getElementById('school-code-div').value = school_code
  document.getElementById('school-textfield').value = school_name
  $('#school-modal').modal('hide')
}

const locationList = () => {
  return new Promise((resolve, reject) => {
    $.ajax({
      type: 'GET',
      url: "https://meal-board.herokuapp.com/school/location",
      dataType: "json",
      data: {},
      success: (response) => {
        return resolve(response.location)
      },
      error: (e) => {
        reject(e)
      }
    })
  })
}

const insertLocation = (location) => {
  let selector = document.getElementById('location-selector')
  for (const [key, value] of Object.entries(location)) {
    let option = document.createElement('option')
    option.value = key
    option.key = value
    option.text = value
    selector.add(option)
  }
}

const meals = () => { // 함수 파라미터로 날짜정보 전달 
  if (checkButtonDisabled()) return
  const selector = document.getElementById('location-selector')
  const regionCode = selector.options[selector.selectedIndex].value
  const yyyymmdd = document.getElementById('current-time').value.split('-').join('')
  const schoolCode = document.getElementById('school-code-div').value
  $.ajax({
    type: "GET",
    url: "https://meal-board.herokuapp.com/meal",
    data: {
      'begin': yyyymmdd,
      'end': yyyymmdd,
      'region_code': regionCode,
      'school_code': schoolCode
    },
    success: function (response) {
      console.log(response.result[yyyymmdd])
      try{
        const mealInfo = response.result[yyyymmdd].DDISH_NM
        const mealCard = document.getElementById('meal-card')
        mealCard.innerHTML = ''
        const listHead = document.createElement('div')
        listHead.classList.add('card-header')
        listHead.classList.add('font-gain-weight')
        const mealName = document.createTextNode(
          document.getElementById('current-time').value
        )
        listHead.appendChild(mealName)
        mealCard.appendChild(listHead)
        for (meal of mealInfo){
          const listItem = document.createElement('li')
          listItem.classList.add('list-group-item')
          listItem.classList.add('text-align-center')
          const mealName = document.createTextNode(meal)
          listItem.appendChild(mealName)
          mealCard.appendChild(listItem)
        }
        const lastListItem = document.createElement('li')
        lastListItem.classList.add('list-group-item')
        const shareButton = document.createElement('button')
        shareButton.classList.add('btn')
        shareButton.classList.add('btn-prirmary')
        shareButton.classList.add('full-width')
        shareButton.innerText = '저장'
        shareButton.setAttribute('onclick', 'saveMeal()')
        lastListItem.appendChild(shareButton)
        mealCard.appendChild(lastListItem)
      } catch(err) {
        const mealCard = document.getElementById('meal-card')
        mealCard.classList.add('font-gain-weight')
        mealCard.classList.add('text-align-center')

        // TODO: 요청은 성공했으나, 데이터 처리중 오류발생할경우 처리
        mealCard.innerHTML = "메뉴정보를 불러올 수 없어요..<br/>\
          아직 교육청에 식단정보가 올라가지 않았어요..\
          <img src='./static/images/keep-calm.jpeg' style='width:50%;')}}>\
        "
      }
    },
    error: (error) => {
      console.log(error)
      const mealCard = document.getElementById('meal-card')
      mealCard.classList.add('font-gain-weight')
      mealCard.classList.add('text-align-center')
      mealCard.innerHTML = "메뉴정보를 불러올 수 없어요..<br/>\
        아직 교육청에 식단정보가 올라가지 않았어요..\
        <img src='./static/images/keep-calm.jpeg' style='width:50%;')}}>\
      "
    }
  })
}

const checkButtonDisabled = () => {
  const check_school_code = document.getElementById('location-selector').value !== '' ? false : true
  const check_school_name = document.getElementById('school-code-div').value !== undefined ? false : true
  const check_date = document.getElementById('current-time').value !== '' ? false : true
  
  if (check_school_code) {
    alert('지역을 선택해주세요')
  } else if (check_school_name) {
    alert('학교명을 확인해주세요')
  } else if (check_date) {
    alert('날짜를 입력해주세요')
  }

  return check_school_name || check_school_code || check_date
}

const saveMeal = () => {
  const mealCard = document.getElementById('meal-card')
  const mealInfo = mealCard.innerText
  const date = document.getElementById('current-time').value
  const schoolName = document.getElementById('school-textfield').value
  const schoolCode = document.getElementById('school-code-div').value
  const regionCode = document.getElementById('location-selector').value
  const regionName = document.getElementById('location-selector').options[document.getElementById('location-selector').selectedIndex].text
  const meal = {
    'date': date,
    'region_code': regionCode,
    'region_name': regionName,
    'school_code': schoolCode,
    'school_name': schoolName,
    'meal_info': mealInfo.split('\n').slice(1, -1).join(',')
  }
  $.ajax({
    type: "POST",
    url: "http://localhost:8086/mypage/meal",
    data: meal,
    success: function (response) {
      console.log(response)
      alert('저장되었습니다')
    },
    error: (error) => {
      window.location.href = "/login"
    }
  })
}


window.onload =  async () => {
  const location = await locationList()
  insertLocation(location)
};


