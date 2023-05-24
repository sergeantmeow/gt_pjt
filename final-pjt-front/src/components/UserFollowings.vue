<template>
  <div>
    <h3 @click="toggleFollowings" class="following-title">팔로잉</h3>
    <ul v-if="showFollowings" class="list-group">
      <li v-for="following in paginatedFollowings" :key="following.id" class="list-group-item">
        <router-link :to="{ name: 'OtherProfileView', params: { username: following.username } }" class="item">
          {{ following.username }}
        </router-link>
      </li>
    </ul>
    <div class="pagination" v-if="showFollowings">
      <div class="pagination-buttons">
        <button v-for="page in pageCount" :key="page" @click="changePage(page, $event)" :class="{ active: currentPage === page }">{{ page }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL;

export default {
  name: 'UserFollowings',
  data() {
    return {
      followings: [],
      showFollowings: false,
      currentPage: 1,
      followingsPerPage: 3,
    };
  },
  props: {
    id: Number,
  },
  computed: {
    paginatedFollowings() {
      const startIndex = (this.currentPage - 1) * this.followingsPerPage;
      const endIndex = startIndex + this.followingsPerPage;
      return this.followings.slice(startIndex, endIndex);
    },
    pageCount() {
      return Math.ceil(this.followings.length / this.followingsPerPage);
    },
  },
  methods: {
    toggleFollowings() {
      if (this.showFollowings) {
        this.showFollowings = false;
      } else {
        this.getFollowings();
      }
    },
    getFollowings() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/${this.id}/followings/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
      })
        .then((response) => {
          this.followings = response.data;
          this.showFollowings = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    changePage(page, event) {
      this.currentPage = page;
      event.preventDefault();
    },
  },
};
</script>

<style scoped>
.following-title {
  transition: transform 0.3s ease;
}
.following-title:hover {
  transform: scale(1.1);
}

.list-group-item {
  border-color: rgb(31, 32, 63, 0);
  background-color: rgb(31, 32, 63, 0);
  color: #bfbfbf;
}

.list-group-item:hover {
  background-color: rgba(79, 61, 99, 0);
  color: #ff2679;
}

.item {
  color: #bfbfbf;
  text-decoration: none;
}

.item:hover {
  color: #ff2679;
}

.pagination {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}

.pagination-buttons {
  display: flex;
  align-items: center;
}

.pagination button {
  margin: 5px;
  padding: 5px 10px;
  background-color: #fff;
  border: 1px solid #ccc;
  color: #333;
  cursor: pointer;
}

.pagination button:hover {
  background-color: #eee;
}

.pagination button.active {
  background-color: #ff2679;
  color: #fff;
}
</style>
