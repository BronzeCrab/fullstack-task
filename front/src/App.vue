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
          label: "ticker_00",
          borderColor: "#3e95cd",
          fill: false
        }
      ]
    }
  }),
  components: { LineChart, TickerDropdown },
  methods: {
    onDropChanged(ticker_name) {
      this.graphData.labels = []
      this.graphData.datasets[0].data = []
      this.graphData.datasets[0].label = ticker_name
      this.socket.close()
      this.get_ticker_value(ticker_name)
    },
    get_ticker_value(ticker_name='ticker_00') {
      this.socket = new WebSocket('ws://localhost:8000/ws/')
      let _this = this
      this.socket.onmessage = function(event) {
        let data = JSON.parse(event.data)
        if (data.message[ticker_name].length > 0) {
          console.log(ticker_name)
          console.log(data.message[ticker_name])
          _this.graphData.labels.push(data.message[ticker_name][1])
          _this.graphData.datasets[0].data.push(data.message[ticker_name][0])
        }
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
