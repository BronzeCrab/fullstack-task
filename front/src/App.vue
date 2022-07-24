<template>
  <header>
    <h3>График стоимости тикеров:</h3>
  </header>

  <main>
    <BarChart />
  </main>
</template>

<script>
import BarChart from '@/components/BarChart.vue'

export default {
  name: 'App',
  components: { BarChart }
}
</script>

<style scoped>
  header {
    text-align: center;
  }
</style>
