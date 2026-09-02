FROM node:lts-slim AS base

FROM ghcr.io/astral-sh/uv:debian AS uv

FROM base

COPY --from=uv /usr/local/bin/uv /usr/local/bin/uv
COPY --from=uv /usr/local/bin/uvx /usr/local/bin/uvx

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        jq \
        make \
        && \
    npm install --global \
        prettier \
        markdownlint-cli2 \
        && \
    rm -rf /var/lib/apt/lists/*

RUN uv python install 3.11 && \
    uv venv --python 3.11 /opt/venv && \
    uv pip install \
        --python /opt/venv/bin/python \
        cffconvert \
        jsonschema \
        pyyaml && \
    printf '%s\n' 'export PATH="/opt/venv/bin:$PATH"' > /etc/profile.d/omf-skills-venv.sh && \
    chmod +x /etc/profile.d/omf-skills-venv.sh

ENV PATH="/opt/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

ENTRYPOINT ["bash", "-lc"]
