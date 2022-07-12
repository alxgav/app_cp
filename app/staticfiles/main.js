
; (function () {

  let today = new Date().toISOString().slice(0, 10)
  let select_date = document.getElementById('day_today')

  select_date.value = today
  console.log(today)


  let order_ = document.getElementById('order_')
  let order_time = document.getElementById('order_time')

  async function get_time() {
    const response = await fetch('http://127.0.0.1:8000/order_time/')
    let data = await response.json()
    data = JSON.parse(data)
    console.log(data)
    // show(data)

  }

  function show(data) {
    for (let i of data) {
      order_.addEventListener('change', (e) => {
        let val = e.target.value
        if (i.pk === val) {
          order_time.value = i.fields.time_job
        }

      })

    }
  }
  get_time()

})()