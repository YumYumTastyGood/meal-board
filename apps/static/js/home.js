const searchSchool = () => {
  const schoolName = document.getElementById('school-textfield').value
  const selector = document.getElementById('location-selector')
  const regionCode = selector.options[selector.selectedIndex].value
  $.ajax({
    type: "GET",
    url: "https://meal-board.herokuapp.com/school",
    data: {
      'location': regionCode,
      'school_name': schoolName
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
        const data = response.location[0]
        return resolve(data)
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
    if (key == '_id') continue
    let option = document.createElement('option')
    option.value = key
    option.key = value
    option.text = value
    selector.add(option)
  }
}

const meals = () => { // ?????? ??????????????? ???????????? ?????? 
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
        shareButton.innerText = '??????'
        shareButton.setAttribute('onclick', 'saveMeal()')
        lastListItem.appendChild(shareButton)
        mealCard.appendChild(lastListItem)
      } catch(err) {
        const mealCard = document.getElementById('meal-card')
        mealCard.classList.add('font-gain-weight')
        mealCard.classList.add('text-align-center')

        // TODO: ????????? ???????????????, ????????? ????????? ????????????????????? ??????
        mealCard.innerHTML = "??????????????? ????????? ??? ?????????..<br/>\
          ?????? ???????????? ??????????????? ???????????? ????????????..\
          <img src='./static/images/keep-calm.jpeg' style='width:50%;')}}>\
        "
      }
    },
    error: (error) => {
      const mealCard = document.getElementById('meal-card')
      mealCard.classList.add('font-gain-weight')
      mealCard.classList.add('text-align-center')
      mealCard.innerHTML = "??????????????? ????????? ??? ?????????..<br/>\
        ?????? ???????????? ??????????????? ???????????? ????????????..\
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
    alert('????????? ??????????????????')
  } else if (check_school_name) {
    alert('???????????? ??????????????????')
  } else if (check_date) {
    alert('????????? ??????????????????')
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
    url: "https://meal-board.herokuapp.com/mypage/meal",
    data: meal,
    success: function (response) {
      alert('?????????????????????')
    },
    error: (error) => {
      window.location.href = "/login"
    }
  })
}


window.onload =  async () => {
  const response = await locationList()
  insertLocation(response)
};


