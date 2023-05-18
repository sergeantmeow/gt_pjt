import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '../views/ArticleView'
import ArticleCreateView from '../views/ArticleCreateView'
import ArticleDetailView from '../views/ArticleDetailView'
import MovieListView from '@/views/MovieListView'
import MovieDetailView from '@/views/MovieDetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/articles/detail',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/MovieList',
    name: 'MovieListView',
    component: MovieListView
  },
  {
    path: '/MovieDetail',
    name: 'MovieDetailView',
    component: MovieDetailView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
