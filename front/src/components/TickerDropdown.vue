<template>
  <div class="ticker_drop">
    <label>Выберете название тикера:</label>
    <select id=ticker-sel name="ticker-names" @change="handler">
      <option v-for="choice in choices">{{ choice }}</option>
    </select>
  </div>
</template>

<script>
  export default {
    name: 'TickerDropdown',
    data: () => ({
      'choices': []
    }),
    methods: {
      handler(event) {
        this.$emit('dropChanged', event.target.value)
      }
    },
    mounted () {
      fetch('http://localhost:8000/ticker_names/')
        .then(response => response.json())
        .then(data => (this.choices = data));
    }
  }
</script>

<style scoped>
  #ticker-sel {
    margin-left: 0.5rem;
  }
</style>