<template>
  <header>
    <h3>График стоимости тикеров:</h3>
  </header>
  <main>
    <TickerDropdown @dropChanged="onDropChanged"/>
    <LineChart />
  </main>
</template>

<script>
import LineChart from '@/components/LineChart.vue'
import TickerDropdown from '@/components/TickerDropdown.vue'

export default {
  name: 'App',
  components: { LineChart, TickerDropdown },
  methods: {
    onDropChanged(ticker_name) {
      console.log(ticker_name)
    }
  }
}
</script>

<style scoped>
  header, .ticker_drop {
    text-align: center;
  }
  .ticker_drop {
    margin-bottom: 1rem;
  }
</style>
