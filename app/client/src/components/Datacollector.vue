<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group 
        id="input-group-1" 
        label="Wat is uw leeftijd?" 
        label-for="input-1"
        description="Omdat we van zowel jongeren als ouderen willen weten wat ze van deze plek vinden, willen we graag uw leeftijd weten. "
        >
        <b-form-input
          id="input-1"
          v-model="form.age"
          placeholder=""
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id=input-group-2 label="Hoe vaak komt u hier?" label-for="input-2" v-slot="{ ariaDescribedby }">
        <b-form-radio-group
        id="radio-group-2"
        v-model="form.frequency"
        :aria-describedby="ariaDescribedby"
        name="radio-sub-component2"
        stacked
        >
          <b-form-radio value="1" variant="primary">Minder dan één keer per maand.</b-form-radio>
          <b-form-radio value="2">Één keer per week</b-form-radio>
          <b-form-radio value="3">Twee keer per week</b-form-radio>
          <b-form-radio value="4">Dagelijks</b-form-radio>
        </b-form-radio-group>
      </b-form-group>


      <b-form-group
        id="input-group-3"
        label="Waarom bent u hier?"
        label-for="input-3"
      >
        <b-form-select
          id="input-3"
          v-model="form.reasonOfVisit"
          placeholder=""
          :options="options"
          required
        ></b-form-select>
      </b-form-group>

    

    <b-form-group
      id="input-group"
      label="Hoe prettig vindt u deze plek? Geef deze plek een aantal sterren! "
      label-for="input-4"      
      >
      <b-form-rating
        id="input-4"
        v-model="form.stars"
        variant="dark"
        required
        >
      </b-form-rating>

    </b-form-group>


    <b-form-group
    id="input-group-5"
    label="Voelt u zich wel eens onveilig op deze plek?"
    labelfor="input-5"
    v-slot="{ ariaDescribedby }"
    required
    >
    
    <b-form-radio-group
        id="radio-group-5"
        v-model="form.safety"
        :aria-describedby="ariaDescribedby"
        name="radio-sub-component5"
        stacked
        >
          <b-form-radio value="1" variant="primary">Ik voel me hier nooit veilig</b-form-radio>
          <b-form-radio value="2">Ik heb me hier ooit een keer onveilig gevoeld</b-form-radio>
          <b-form-radio value="3">Ik voel me hier meestal veilig</b-form-radio>
          <b-form-radio value="4">Ik voel me hier altijd veilig </b-form-radio>
        </b-form-radio-group>
      
    


    </b-form-group>
      <b-form-group
        id="input-group-6"
        label="Wat kan de gemeente doen om deze plaats te verbeteren?"
        label-for="input-6"
        description="Voorbeeld: Haal vaker het afval op. De container is vaak vol."
      >
        <b-form-textarea
          id="input-6"
          v-model="form.feedback"
          placeholder=""
          required
        ></b-form-textarea>
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
          age: 10,
          frequency: null,
          reasonOfVisit: '',
          stars: '',
          feedback: '',
          safety: null,
          qr_id: new URL(location.href).searchParams.get('qr_id'),
        },
        options: [
          {value: "wandelen", text:"Ik kom hier een frisse neus halen"},
          {value: "onderweg", text:"Ik ben onderweg"},
          {value: "wonen", text:"Ik woon hier in de buurt"},
          {value: "anders", text:"Overig"},
        ],
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        // alert(JSON.stringify(this.form))
        axios({method: 'post',
               url: 'https://challenges.social/api/feedback/',
               headers: {
                 'Content-Type': 'application/json',
                 },
               data: this.form 
              })
              .then(
                  (response) => {console.log(response)}
              );
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

<style scoped>

</style>