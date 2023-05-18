<template>
  <div class="article-list">
    <h3>Article List</h3>
    <template v-if="articles.length">
    <ArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
    </template>
    <template v-else>
      <p>게시글이 아직 아무것도 없습니다.</p>
    </template>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
