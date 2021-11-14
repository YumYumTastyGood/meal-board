const replaceMessage = () => {
  const messageHeadline = document.getElementById('user-message-headline')
  const messageInput = document.getElementById('user-message-input')
  messageHeadline.style.display = 'none'
  messageInput.style.display = 'block'
}

const submitMessage = async () => {
  const messageInput = document.getElementById('user-message-input')
  const messageHeadline = document.getElementById('user-message-headline')
  xhr = new XMLHttpRequest()
  const data = {
    message: messageInput.value
  }
  await xhr.open('POST', '/mypage/message', true)
  await xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.onload = () => {
    if (xhr.status === 200) {
      messageHeadline.innerText = messageInput.value
    } else {
      console.error(xhr.responseText)
    }
  }
  await xhr.send(JSON.stringify(data))
  messageInput.style.display = 'none'
  messageHeadline.style.display = 'block'
}

const replaceNickname = () => {
  const nicknameHeadline = document.getElementById('user-nickname-headline')
  const nicknameInput = document.getElementById('user-nickname-input')
  nicknameHeadline.style.display = 'none'
  nicknameInput.style.display = 'block'
}

const submitNickname = async () => {
  const nicknameInput = document.getElementById('user-nickname-input')
  const nicknameHeadline = document.getElementById('user-nickname-headline')
  xhr = new XMLHttpRequest()
  const data = {
    nickname: nicknameInput.value
  }
  await xhr.open('POST', '/mypage/name', true)
  await xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.onload = () => {
    if (xhr.status === 200) {
      nicknameHeadline.innerText = nicknameInput.value
    } else {
      console.error(xhr.responseText)
    }
  }
  await xhr.send(JSON.stringify(data))
  nicknameInput.style.display = 'none'
  nicknameHeadline.style.display = 'block'

}

const getMyMealInfo = async () => {
  xhr = new XMLHttpRequest()
  await xhr.open('GET', '/mypage/meal', true)
  xhr.onload = () => {
    if (xhr.status === 200) {
      const mealInfo = JSON.parse(xhr.responseText)
      myMealTable = document.getElementById('my-meals')
      JSON.parse(mealInfo.meals).forEach(meal => {
        const mealLabelRow = document.createElement('div')
        mealLabelRow.className = 'meal-label row'
        const mealLabelColDate = document.createElement('div')
        mealLabelColDate.className = 'meal-label-date col-md-2 col-xg-2 background-gray font-get-weight'
        mealLabelColDate.innerText = `${meal.date}`
        const mealLabelColName = document.createElement('div')
        mealLabelColName.className = 'meal-label-name col-md-2 col-xg-2 background-gray font-get-weight'
        mealLabelColName.innerText = `${meal.school_name}`
        mealLabelRow.appendChild(mealLabelColDate)
        mealLabelRow.appendChild(mealLabelColName)
        const mealRow = document.createElement('div')
        mealRow.className = 'meal-info row put-padding-bottom'
        mealRow.id = `${meal.user_id}_${meal.region_code}_${meal.school_code}_${meal.date}`
        meal.meal_info.forEach(mealInfo => {
          const mealCol = document.createElement('div')
          mealCol.className = 'col-md'
          mealCol.innerText = mealInfo
          mealRow.appendChild(mealCol)
        })
        myMealTable.appendChild(mealLabelRow)
        myMealTable.appendChild(mealRow)
      })
    } else {
      console.error(xhr.responseText)
    }
  }
  await xhr.send()
}

window.onload =  async () => {
  await getMyMealInfo()
};
