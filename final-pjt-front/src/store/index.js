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
    cinemaMovies: [
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

    GET_MOVIES_CINEMA(state, cinemaMovies){
      state.cinemaMovies = cinemaMovies
      // console.log('voila')
      // console.log(cinemaMovies)
    },

  },
  actions: {
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then((response)=>{
      let twentyData = [];
      let idx = [];
      for(let i=0; i<20; i++){
          let goFlag = true;
          let tmpNum = Math.floor(Math.random() * response.data.length)
          for(let j=0; j<idx.length; j++){
            if(tmpNum ==idx[j]){
              goFlag = false
              i--
              break
            }
          }
          if(goFlag){
            idx.push(tmpNum)
            twentyData.push(response.data[tmpNum])
          }
        }
        context.commit('GET_MOVIES', twentyData)
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    getMoviesCinema(context){
      const API_URL = 'http://api.themoviedb.org/3/movie/now_playing'
      axios({
        url: API_URL,
        params: {
          api_key : 'ce3376151cdca276068439ff358212cb',
          language : 'en-US',
          page : 1
        }
      })
      .then((response)=>{
        context.commit('GET_MOVIES_CINEMA', response.data.results)
        // console.log(response.data.results)
      })
      .catch((err)=>{
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
