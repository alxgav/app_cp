window.addEventListener('DOMContentLoaded', () => {
  let today = new Date().toISOString().slice(0, 10)

  let select_date = document.getElementById('day_today')
  
  if (select_date != null) {
    select_date.value = today
  }
  // if (document.getElementById('day_form') != null){
  //   document.getElementById('day_form').value = today
  // }

  
 

  let order_ = document.getElementById('order_')
  

  if (order_ != null) {
    let order_time = document.getElementById('order_time')
    // let select_date = document.getElementById('day_form')
    // select_date.value = today
    // console.log(select_date.value)

    async function get_time() {
      const response = await fetch('http://127.0.0.1:8000/order_time/')
      let data = await response.json()
      data = JSON.parse(data)
      
      show(data)

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
  }


})