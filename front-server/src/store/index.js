import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
    ],
  },
  getters: {
  },
  mutations: {
    GET_JSON(state, movieItems){
      state.movieItems = movieItems
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
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
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
