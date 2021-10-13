<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="What do you think about this place?"
        label-for="input-1"
        description="Example: The trees here look nice."
      >
        <b-form-input
          id="input-1"
          v-model="form.feedback"
          placeholder=""
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Age:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.age"
          placeholder="Enter your age"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    data() {
      return {
        form: {
          feedback: '',
          age: 10,
          qr_name: '12',
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        // alert(JSON.stringify(this.form))
        axios({method: 'post',
               url: 'localhost:8000/feedback',
               headers: {
                 'Content-Type': 'application/json',
                 },
               data: this.form 
              }).then(
                  (response) => console.log(response)
              )
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.food = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>