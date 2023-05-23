<template>
  <div>
    <h3 class="text-center mb-4" @click="toggleArticles">작성한 글</h3>
    <ul class="list-group" v-if="showArticles">
      <li class="list-group-item" v-for="article in displayedArticles" :key="article.id">
        <router-link :to="{ name: 'ArticleDetailView', params: { id: article.id }}" class="article-title">
          <h5>{{ article.title }}</h5>
        </router-link>
        <p>{{ formatDateTime(article.created_at) }}</p>
      </li>
    </ul>

    <nav v-if="totalPages > 1 && showArticles">
      <ul class="pagination justify-content-center mt-4">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <a class="page-link" href="#" @click="changePage(currentPage - 1, $event)" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: currentPage === page }">
          <a class="page-link" href="#" @click="changePage(page, $event)">{{ page }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <a class="page-link" href="#" @click="changePage(currentPage + 1, $event)" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'UserArticle',
  data() {
    return {
      articles: [],
      currentPage: 1,
      itemsPerPage: 3,
      showArticles: false,
    };
  },
  props: {
    username: String,
  },
  created() {
    this.fetchUserArticles();
  },
  computed: {
    totalPages() {
      return Math.ceil(this.articles.length / this.itemsPerPage);
    },
    displayedArticles() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.articles.slice(startIndex, endIndex);
    },
  },
  methods: {
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    fetchUserArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.username}/articles/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
      })
        .then(response => {
          this.articles = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    changePage(page, event) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
        event.preventDefault();
      }
    },
    toggleArticles() {
      this.showArticles = !this.showArticles;
      if (this.showArticles) {
        this.fetchUserArticles();
      }
    },
  },
};
</script>

<style scoped>
.list-group-item {
  border-color: rgb(31, 32, 63);
  background-color: rgb(31, 32, 63);
  color: #bfbfbf;
}

.list-group-item:hover {
  background-color: #4f3d63;
}

.article-title {
  text-decoration: none;
  color: #ff2679;
}

.article-title:hover {
  color: #7c6891;
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
