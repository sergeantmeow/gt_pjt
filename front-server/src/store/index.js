import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
    GET_JSON(state, movieItems){
      state.movieItems = movieItems
    },
  },
  actions: {
    getJson(context){
      const API_URL = "https://api.themoviedb.org/3/movie/top_rated"
      
      axios({
        url: API_URL,
        params: {
          api_key : 'ce3376151cdca276068439ff358212cb',
          language : 'en-US',
          page : 1
        }
      })
      .then((response)=>{
        context.commit('GET_JSON', response.data.results)
      })
      .catch((err)=>{
        console.log('>>>Error Occurred<<<')
        console.log(err)
      })
    },
  },
  modules: {
  }
})
