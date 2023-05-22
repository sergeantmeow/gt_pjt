<template>
  <div class="article-list">
    <template v-if="articles.length">
      <ArticleListItem v-for="article in displayedArticles" :key="article.id" :article="article" />
    </template>
    <template v-else>
      <p>게시글이 아직 없습니다.</p>
    </template>
    <nav v-if="hasPagination" aria-label="Page navigation">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ 'disabled': currentPage === 1 }">
          <button class="page-link" @click="previousPage" :disabled="currentPage === 1">이전</button>
        </li>
        <li class="page-item" v-for="page in totalPages" :key="page" :class="{ 'active': currentPage === page }">
          <button class="page-link" @click="changePage(page)">{{ page }}</button>
        </li>
        <li class="page-item" :class="{ 'disabled': currentPage === totalPages }">
          <button class="page-link" @click="nextPage" :disabled="currentPage === totalPages">다음</button>
        </li>
      </ul>
    </nav>
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
    },
    itemsPerPage() {
      return 5 // 페이지당 아이템 수는 5로 설정
    },
    displayedArticles() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage
      const endIndex = startIndex + this.itemsPerPage
      return this.articles.slice(startIndex, endIndex)
    },
    totalPages() {
      return Math.ceil(this.articles.length / this.itemsPerPage)
    },
    hasPagination() {
      return this.totalPages > 1
    },
  },
  methods: {
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
      }
    },
    changePage(page) {
      this.currentPage = page
    },
  },
  data() {
    return {
      currentPage: 1, // 초기 페이지 번호는 1로 설정
    }
  },
}
</script>

<style scoped>
.article-list {
  text-align: center;
  padding: 20px;
}

.pagination {
  margin-top: 20px;
}

.page-item.disabled .page-link {
  background-color: #4f3d63;
  border-color: #4f3d63;
  color: #ff2679;
  cursor: not-allowed;
}

.page-item.active .page-link {
  background-color: #4f3d63;
  border-color: #4f3d63;
  color: #ff2679;
}

.page-link {
  color: #bfbfbf;
  border-radius: 0;
}

.page-link:hover {
  background-color: #4f3d63;
  border-color: #261639;
  color: #ff2679;
}
</style>
