<template>
  <header>
    <h3>График стоимости тикеров:</h3>
  </header>
  <main>
    <TickerDropdown />
    <BarChart />
  </main>
</template>

<script>
import BarChart from '@/components/BarChart.vue'
import TickerDropdown from '@/components/TickerDropdown.vue'

export default {
  name: 'App',
  components: { BarChart, TickerDropdown }
}
</script>

<style scoped>
  header, .ticker_drop {
    text-align: center;
  }
  .ticker_drop {
    margin-bottom: 2rem;
  }
</style>
