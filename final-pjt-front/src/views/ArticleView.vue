<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'ArticleCreateView' }">[CREATE]</router-link>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')     
    }
  }
}
</script>

<style>

</style>
