import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '../views/ArticleView'
import ArticleCreateView from '../views/ArticleCreateView'
import ArticleDetailView from '../views/ArticleDetailView'
import MovieListView from '@/views/MovieListView'
import LogInView from '../views/LogInView'
import SignUpView from '../views/SignUpView'
import MyProfileView from '@/views/MyProfileView'

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
    path: '/articles/detail/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },

  {
    path: '/MovieList',
    name: 'MovieListView',
    component: MovieListView
  },
  
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



export default router

