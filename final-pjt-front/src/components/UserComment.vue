<template>
  <div>
    <h3 class="text-center mb-4" @click="toggleComments">작성한 댓글</h3>
    <ul class="list-group" v-if="showComments">
      <li class="list-group-item" v-for="comment in displayedComments" :key="comment.id">
        <p>{{ comment.content }}</p>
      </li>
    </ul>

    <nav v-if="totalPages > 1 && showComments">
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
  name: 'UserComment',
  data() {
    return {
      comments: [],
      currentPage: 1,
      itemsPerPage: 3,
      showComments: false,
    };
  },
  props: {
    username: String,
  },
  created() {
    this.fetchUserComments();
  },
  computed: {
    totalPages() {
      return Math.ceil(this.comments.length / this.itemsPerPage);
    },
    displayedComments() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.comments.slice(startIndex, endIndex);
    },
  },
  methods: {
    fetchUserComments() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.username}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
      })
        .then(response => {
          this.comments = response.data;
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
    toggleComments() {
      this.showComments = !this.showComments;
      if (this.showComments) {
        this.fetchUserComments();
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
  color: #ff2679;
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
