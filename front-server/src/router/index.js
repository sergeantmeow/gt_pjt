import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '../views/ArticleView'
import ArticleCreateView from '../views/ArticleCreateView'
import ArticleDetailView from '../views/ArticleDetailView'
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
