<template>
  <header>
    <h3>График стоимости тикеров:</h3>
  </header>
  <main>
    <TickerDropdown @dropChanged="onDropChanged"/>
    <LineChart :graphData="this.graphData"/>
  </main>
</template>

<script>
import LineChart from '@/components/LineChart.vue'
import TickerDropdown from '@/components/TickerDropdown.vue'

export default {
  name: 'App',
  data: () => ({
    'graphData': {
      labels: [],
      datasets: [
        {
          data: [],
          label: "Ticker",
          borderColor: "#3e95cd",
          fill: false
        }
      ]
    }
  }),
  components: { LineChart, TickerDropdown },
  methods: {
    onDropChanged(ticker_name) {
      console.log(ticker_name)
    },
    get_ticker_value(ticker_name='ticker_00') {
      let socket = new WebSocket('ws://localhost:8000/ws/')
      let _this = this
      socket.onmessage = function(event) {
        let data = JSON.parse(event.data)
        _this.graphData.labels.push('test')
        _this.graphData.datasets[0].data.push(data.message[ticker_name])
      }
    }
  },
  mounted () {
    this.get_ticker_value()
  }
}
</script>

<style scoped>
  header {
    text-align: center;
  }
</style>
