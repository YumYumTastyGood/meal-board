const write_new_meal = async () =>{
  const data = {
    title: document.getElementById('meal-title').value,
    content: document.getElementById('meal-content').value
  }
  xhr = new XMLHttpRequest()
  await xhr.open('POST', '/community/write', true)
  await xhr.setRequestHeader('Content-Type', 'application/json')

  xhr.onload = () => {
    if (xhr.status === 200) {
      location.href = '/community'
    } else {
      alert('잠시 후 다시 시도해주세요')
    }
  }
  await xhr.send(JSON.stringify(data))
}
