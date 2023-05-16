import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
    ],
    movies: [
    ],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    GET_MOVIES(state, movies){
      state.movies = movies
    },
  },
  actions: {
    getMovies(context){
      console.log('>>>>reached getMovies function<<<<')
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then((response)=>{
        console.log('>>>>Got the Data<<<<')
        context.commit('GET_MOVIES', response.data.results)
      })
      .catch((err)=>{
        console.log('>>>>Error Occurred<<<<')
        console.log(err)
      })
    },

    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
      })
        .then((res) => {
        console.log(res, context)
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
