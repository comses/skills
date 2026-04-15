---
name: hpc
description: |
  Generate Slurm job scripts, job arrays, and resource allocation templates for running 
  computational models on HPC (High-Performance Computing) clusters.
  
  Use this skill when you need multi-node execution, high-memory jobs, GPU/accelerator access, 
  or direct Slurm cluster submission. Triggers: "run on HPC", "generate Slurm script", 
  "set up batch array job", "submit to cluster", "create Slurm job array".
  
  Expected output: Slurm batch scripts (.slurm), job array configurations, resource allocation 
  templates, and submission validation checklist.
license: MIT
compatibility: Requires Slurm job scheduler; HPC cluster account
metadata:
  domain: computational-modeling
  maturity: beta
  audience: modelers, researchers
  category: execution
---

# HPC Slurm Scaffolder Skill

## When to Use This Skill

Use this skill when:

- You have computational models that require multi-node parallelism or significant memory
- You need to execute many parameter combinations across an HPC cluster (job arrays)
- You want to leverage GPUs, specialized accelerators, or high-memory nodes
- You require direct queue submission and resource control via Slurm
- You need to coordinate dependent jobs or chain simulations together

## Key Inputs

This skill works best with:

- **Model executable or script** (MPI-enabled application, Python/R script, or shell command)
- **Parallelization strategy** (single-node multi-core, multi-node MPI, embarrassingly parallel)
- **Resource requirements** (CPU cores, memory per node, GPU count, wall-clock time)
- **Job array configuration** (number of jobs, parameter range or sweep specification)
- **Module dependencies** (compilers, libraries, runtime environments loaded via `module load`)
- **HPC cluster specifics** (partition names, queue limits, storage paths)

## Step-by-Step Instructions

### 1. Understand Your Model's Parallelism

Determine how your model scales:

- **Single-node, multi-core:** Uses OpenMP or Python multiprocessing; request 4-32 cores per node
- **Multi-node MPI:** Uses MPI (Message Passing Interface); request 2+ nodes and ensure MPI runtime is available
- **Embarrassingly parallel:** Independent jobs (parameter sweep); use job arrays
- **GPU-accelerated:** Uses CUDA/OpenCL; request GPU resources in Slurm script

### 2. Set Resource Requests

Define resource needs:

```bash
# Example resource profile
#SBATCH --nodes=2              # 2 compute nodes
#SBATCH --ntasks-per-node=16   # 16 MPI processes per node (32 total)
#SBATCH --cpus-per-task=1      # 1 CPU core per MPI task
#SBATCH --mem=64GB             # 64 GB per node
#SBATCH --time=04:00:00        # 4-hour wall-clock limit
#SBATCH --partition=standard   # queue name (cluster-specific)
#SBATCH --gres=gpu:2           # 2 GPUs (if needed)
```

### 3. Generate Slurm Batch Script

The skill creates a `.slurm` script that:

- Loads required modules (compilers, libraries, runtime)
- Sets environment variables (OMP threads, MPI settings)
- Stages input data from shared storage
- Runs your model using srun (for MPI) or local execution
- Copies results back to persistent storage

### 4. Set Up Job Arrays for Parameter Sweeps

For parameter sweeps, use Slurm job arrays:

```bash
#SBATCH --array=1-100%10    # 100 jobs, max 10 running simultaneously
```

Each job receives a unique `$SLURM_ARRAY_TASK_ID` to index parameter combinations:

```bash
# In your script:
params=$(sed -n "${SLURM_ARRAY_TASK_ID}p" parameters.txt)
python model.py $params --output results_${SLURM_ARRAY_TASK_ID}.csv
```

The skill generates:

- **Slurm submit script** (.slurm)
- **Parameter list** (one per line, one parameter set per job)
- **Array submission command** ready to run

### 5. Validate Before Submission

Check your job script:

```bash
python scripts/validate_slurm.py my_job.slurm
# Checks for:
# - Valid Slurm directives
# - Resource requests (not exceeding cluster limits)
# - Module availability
# - Executable and input files
# - Output directory writeable
```

Address warnings before submitting.

### 6. Submit and Monitor

```bash
sbatch my_job.slurm           # Submit single job
sbatch --array=1-100 my_job.slurm   # Submit job array
squeue -u $USER               # Check job status
scancel $JOBID                # Cancel job
```

## ⚠️ Gotchas

- **Module availability:** HPC clusters vary widely. Modules differ by cluster (XSEDE, Summit, Bridges, etc.). Confirm module names with `module avail` before scripting.
- **Storage paths:** Use cluster-specific paths: `/home/` for home, `/scratch/` for fast local storage, `/data/` for shared storage. Understand quotas and retention policies.
- **Wall-clock time:** Underestimate penalties for exceeding wall-clock limits. If your model might run long, add buffer (1.5× estimated time) and implement checkpointing.
- **Memory oversubscription:** Request memory conservatively. If you request 128GB and only use 10GB, you waste resources and delay job start.
- **MPI initialization:** Multi-node MPI jobs require careful process placement. Use `srun` for MPI jobs, not direct executable invocation.
- **GPU scheduling:** GPUs are scarce. Share them when possible; request only what you need. Some clusters oversubscribe GPUs (multiple jobs per GPU).
- **Job dependency chains:** If you have dependent jobs (e.g., pre-processing → simulation → analysis), use `sbatch --dependency` to coordinate them.

## Templates & Resources

- **Slurm Basics:** See `references/SLURM-QUICKSTART.md` for cluster commands and job submission
- **Slurm vs HTCondor:** See `references/CONDOR-VS-SLURM.md` for environment comparison
- **Validation script:** Use `scripts/validate_slurm.py` to check your job configuration
- **Batch script template:** See `assets/slurm-template.slurm` for basic structure
- **Job array template:** See `assets/slurm-array-template.slurm` for parameter sweeps
- **MPI job example:** See `examples/mpi-job.slurm` for multi-node execution
- **GPU job example:** See `examples/gpu-job.slurm` for GPU-accelerated work

## Example

**Input:** Python model with parameter sweep over 100 combinations, estimated 10 min per job

**Output:**

1. **Slurm batch script** (`param_sweep.slurm`):
   ```bash
   #!/bin/bash
   #SBATCH --job-name=param_sweep
   #SBATCH --array=1-100%20
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=4
   #SBATCH --mem=16GB
   #SBATCH --time=00:30:00
   #SBATCH --output=logs/sweep_%a.out
   #SBATCH --error=logs/sweep_%a.err
   
   module load python/3.10
   cd $SLURM_SUBMIT_DIR
   
   params=$(sed -n "${SLURM_ARRAY_TASK_ID}p" params.txt)
   python model.py $params --output results_${SLURM_ARRAY_TASK_ID}.csv
   ```

2. **Parameter list** (`params.txt`, 100 lines):
   ```
   --pop 10 --patches 5 --seed 1001
   --pop 10 --patches 5 --seed 1002
   --pop 10 --patches 10 --seed 1001
   ...
   --pop 100 --patches 20 --seed 1005
   ```

3. **Submission & monitoring:**
   ```bash
   $ sbatch --array=1-100%20 param_sweep.slurm
   Submitted batch job 12345
   
   $ squeue -u $USER
   JOBID  PARTITION  NAME  USER  ST  TIME  NODES  NODELIST(REASON)
   12345_1  standard  param_sweep  user  R  00:05  1  node01
   12345_2  standard  param_sweep  user  R  00:03  1  node02
   12345_3  standard  param_sweep  user  PD  0:00  1  (Priority)
   ...
   ```

---

## Quick Reference

| Task | Command/Reference |
|------|---|
| Validate Slurm script | `python scripts/validate_slurm.py` |
| Slurm quickstart | See `references/SLURM-QUICKSTART.md` |
| Slurm vs HTCondor | See `references/CONDOR-VS-SLURM.md` |
| Job array examples | See `examples/slurm-array-template.slurm` |
| MPI examples | See `examples/mpi-job.slurm` |

---

For community feedback or issues, see the [COMSES Skills](https://github.com/comses-network/skills) repository.
