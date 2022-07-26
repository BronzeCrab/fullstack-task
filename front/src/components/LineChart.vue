<template>
  <Line :chart-data="datacollection" class="line-chart"/>
  <h1>{{values}}</h1>
</template>

<script>
import { Line } from 'vue-chartjs'
import 'chart.js/auto'

export default {
  name: 'LineChart',
  props: ['graphData'],
  components: {
    Line
  },
  data() {
    return {
      datacollection: this.graphData
    }
  }
}

</script>

<style scoped>
  #ticker-sel {
    margin-left: 0.5rem;
  }

  .line-chart {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  }
</style>